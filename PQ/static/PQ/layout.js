const isScrolling = () => {
    const headerEl = document.querySelector('.primary-header')
    let windowPosition = window.scrollY > 100 
    headerEl.classList.toggle('active', windowPosition)
}

document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', isScrolling)
})



