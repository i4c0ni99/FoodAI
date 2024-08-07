import { KalMacroCalculator } from "../component/kalMacroCalulator.component"

import { calculateKalMacro } from "../utils/calcoloKalMacro.utils"
import { setUserCookie } from "../utils/cookies.service"
interface Data {
    eta: number,
    altezza: number,
    peso: number
    obbiettivo:string,
    stile_di_vita:string,
    numero_di_pasti:number
}
export const Calculator = () =>{
    return (<KalMacroCalculator onSubmission={async (data: Data)=>{
        let allData=calculateKalMacro(data) 
        console.log(allData)
        setUserCookie({
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena':allData.pasti.cena,
            'colazione':allData.pasti.colazione,
            'pranzo':allData.pasti.pranzo,
            'spuntino_mat':allData.pasti.spuntino_mat,
            'spuntino_pom':allData.pasti.spuntino_pom
        })
        window.location.href='/preferer-aliment'
    }}></KalMacroCalculator>)
}