const hideSidebar = ()=>{
    const sidebar = document.getElementById("sidebarToggle");
    const toggleButton = document.querySelector(".navButtonOut");
    sidebar.classList.toggle("hidden");
        if (sidebar.classList.contains("hidden")) {
            toggleButton.style.display = "block";
        } else {
            toggleButton.style.display = "none";
        }
    }
    
    



    document.addEventListener("DOMContentLoaded", () => {
        document.querySelector(".navButton").addEventListener("click", function() {
        console.log("navButton (toggle sidebar) clicked");
        document.querySelector(".dashboard-container").style.gridTemplateColumns = "1fr";
        document.querySelector(".navButton")

    });
            document.querySelector('.navButtonOut').addEventListener('click', function(){
                const toggleButton = document.querySelector(".navButtonOut");
                const sidebar = document.getElementById("sidebarToggle");
                const isHidden = sidebar.classList.toggle("hidden");
                if (isHidden) {
                    document.querySelector(".dashboard-container").style.gridTemplateColumns = "1fr";
                    toggleButton.style.display = "block";
                } else {
                    document.querySelector(".dashboard-container").style.gridTemplateColumns = "250px 1fr";
                    toggleButton.style.display = "none";
                }
        });
});