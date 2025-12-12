 function toggleDropdown(id){
    const settingsContent = document.getElementById(`${id}`);
    settingsContent.style.display = (settingsContent.style.display === "flex") ? "none" : "flex";
    // if(settingsContent.style.display === 'none' || settingsContent.style.display === ''){
    //     settingsContent.style.display = 'flex';
    //     // decision = false
    //     console.log("button clicked show")
    // }
    // else{
    //     settingsContent.style.display = 'none';
    //     console.log("button clicked hidden")
    // }
}