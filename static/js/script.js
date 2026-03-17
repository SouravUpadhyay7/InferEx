/* ============================================================
   InferEx — script.js
   Handles: category filter chips, live search, URL pre-filter
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {

    /* ── Filtering + Search (explore page) ─────────────────── */
    const filterBtns  = document.querySelectorAll('.filter-btn');
    const modelCards  = document.querySelectorAll('.model-card');
    const searchInput = document.getElementById('modelSearch');

    let activeFilter = 'all';
    let searchTerm   = '';

    function applyFilters() {
        modelCards.forEach((card, i) => {
            const cat    = card.getAttribute('data-category') || '';
            const name   = card.getAttribute('data-name')     || '';
            const catOk  = activeFilter === 'all' || cat === activeFilter;
            const nameOk = name.includes(searchTerm);

            if (catOk && nameOk) {
                card.style.display = 'flex';
                // Re-trigger entrance animation
                card.style.animation = 'none';
                card.offsetHeight; // reflow
                card.style.animation = '';
                card.style.animationDelay = `${i * 0.04}s`;
            } else {
                card.style.display = 'none';
            }
        });
    }

    if (filterBtns.length > 0 && modelCards.length > 0) {

        /* Sync button active state */
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                activeFilter = btn.getAttribute('data-filter');
                applyFilters();
            });
        });

        /* Live search */
        if (searchInput) {
            searchInput.addEventListener('input', () => {
                searchTerm = searchInput.value.trim().toLowerCase();
                applyFilters();
            });
        }

        /* Pre-filter from URL query string: /explore?category=NLP+Projects */
        const params = new URLSearchParams(window.location.search);
        const urlCat = params.get('category');
        if (urlCat) {
            filterBtns.forEach(btn => {
                if (btn.getAttribute('data-filter') === urlCat) {
                    btn.click();
                }
            });
        }
    }

    /* ── Navbar scroll shadow ───────────────────────────────── */
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    /* ── Smooth card hover tilt effect ─────────────────────── */
    document.querySelectorAll('.model-card, .cat-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect   = card.getBoundingClientRect();
            const x      = e.clientX - rect.left;
            const y      = e.clientY - rect.top;
            const midX   = rect.width  / 2;
            const midY   = rect.height / 2;
            const rotateX = ((y - midY) / midY) * -5;
            const rotateY = ((x - midX) / midX) *  5;
            card.style.transform = `translateY(-10px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });
});
