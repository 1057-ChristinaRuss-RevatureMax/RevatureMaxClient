// This is where the javascript would go
// Select the elements that contains the tab
const tabs = document.querySelectorAll('[data-tab-target]');
const tabContent = document.querySelectorAll('[data-tab-content]');
// Loops through the elements every time it's click, show the content
tabs.forEach(tab => {
    tab.addEventListener('click', () =>{
        // Get the tab element dashboard, statistics, settings
        const target = document.querySelector(tab.dataset.tabTarget);
        // Remove active class
        tabContent.forEach(tabContent => {
            tabContent.classList.remove('active')
        });
        tabs.forEach(tab => {
            tab.classList.remove('active')
        });
        tab.classList.add("active");
        target.classList.add("active");
    });
});