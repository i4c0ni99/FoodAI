import Cookies from 'js-cookie'

export const getCookie = (str: string) => {
    const result = Cookies.get(str)

    if(result){
        return JSON.parse(result);
    }
    
}

export const setUserCookie = (calMacro:{}) => {
    Cookies.set('calMacro&aliments', JSON.stringify(calMacro))
    window.location.reload()
}

export const setDietCookie = ( daily_diet:{}) => {
   Cookies.set('daily_diet',JSON.stringify(daily_diet))
}

