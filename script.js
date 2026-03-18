function toggleMenu() {
    const sidebar = document.getElementById('sidebarMenu');
    const backdrop = document.querySelector('.menu-backdrop');

    sidebar.classList.toggle('active');
    backdrop.classList.toggle('active');
}