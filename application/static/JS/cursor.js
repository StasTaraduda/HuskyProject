var confirmStorage = true
window.addEventListener('beforeunload', saveScrolling)
document.addEventListener('DOMContentLoaded', loadScrolling)
function storageAvailable(type) {
    try {
        var storage = window[type];
        value = '__storage_test__';
        storage.setItem(value, value);
        storage.removeItem(value);
        return true;
    }
    catch(e) {
        return false;
    }
}

if (storageAvailable('localStorage')) {
    confirmStorage = confirm('Чи дозволяєте ви зберегти ваші дані у локальне сховище?')
}
else {
    alert('Вибачте, але локальне сховище недоступно')
    
}


function saveScrolling(){
    var pageScroll = document.documentElement.scrollTop || document.body.scrollTop || 0
    // var getScroll = pageScroll - document.documentElement.clientTop
    console.log(pageScroll)
    if(confirmStorage){
        localStorage['scroll'] = JSON.stringify(pageScroll)
        if(document.documentElement.scrollHeight - document.documentElement.scrollTop === document.documentElement.clientHeight){
            localStorage.removeItem('scroll')

        }
    
    }
    else{
        localStorage.removeItem('scroll')
    }
}

function loadScrolling(){
    var scroll = JSON.parse(localStorage.getItem('scroll'))
    if(scroll){
        window.scrollTo(0,scroll)
    }


}