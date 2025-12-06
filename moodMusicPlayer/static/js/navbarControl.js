 function toggleSettingDropdown(){
    let decision = true
    const settingsContent = document.getElementById('settingsDropdown');
    if(settingsContent.style.visibility === 'hidden'){
        settingsContent.style.visibility = 'visible';
        // decision = false
        console.log("button clicked show")
    }
    else{
        settingsContent.style.visibility = 'hidden';
        console.log("button clicked hidden")
    }
}