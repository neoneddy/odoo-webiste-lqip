
odoo.define('website_image_lqip.lazy_loader', function (require) {
    document.addEventListener('DOMContentLoaded', function () {
        const lazyImages = document.querySelectorAll('img.lazy-blur');
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy-blur');
                    observer.unobserve(img);
                }
            });
        });
        lazyImages.forEach(img => observer.observe(img));
    });
});
