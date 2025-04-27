import Cookies from 'js-cookie'

export const getCookie = () => {
    const result = Cookies.get('calMacro')

    if(result){
        console.log(result)
        return JSON.parse(result);
    }
    
}

export const setUserCookie = (calMacro:{}) => {
    Cookies.set('calMacro', JSON.stringify(calMacro))
    window.location.reload()
}



