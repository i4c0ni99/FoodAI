import { IODiet } from "../page/chatAI.page"
import { axiosInstance } from "./axoisInstance.utils"
import { getCookie } from "./cookies.service"

const allData = getCookie('calMacro&aliments')


export async function serverRequestSpuntino_mat() : Promise<IODiet> {
    const axiosResult = await axiosInstance.post('/spuntino_mat',
        {
            'aliments': allData.aliments,
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena': allData.cena,
            'colazione': allData.colazione,
            'pranzo': allData.pranzo,
            'spuntino_mat': allData.spuntino_mat,
            'spuntino_pom': allData.spuntino_pom
        }

    )

    return  axiosResult.data
}

export async function serverRequestPranzo() : Promise<IODiet> {
    const axiosResult = await axiosInstance.post('/pranzo',
        {
            'aliments': allData.aliments,
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena': allData.cena,
            'colazione': allData.colazione,
            'pranzo': allData.pranzo,
            'spuntino_mat': allData.spuntino_mat,
            'spuntino_pom': allData.spuntino_pom
        }

    )

    return  axiosResult.data
}

export async function serverRequestSpuntino_pom() : Promise<IODiet> {
    const axiosResult = await axiosInstance.post('/spuntino_pom',
        {
            'aliments': allData.aliments,
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena': allData.cena,
            'colazione': allData.colazione,
            'pranzo': allData.pranzo,
            'spuntino_mat': allData.spuntino_mat,
            'spuntino_pom': allData.spuntino_pom
        }

    )

    return axiosResult.data
}
export async function serverRequestCena(): Promise<IODiet> {
    const axiosResult = await axiosInstance.post('/pranzo',
        {
            'aliments': allData.aliments,
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena': allData.cena,
            'colazione': allData.colazione,
            'pranzo': allData.pranzo,
            'spuntino_mat': allData.spuntino_mat,
            'spuntino_pom': allData.spuntino_pom
        }


    )

    return  axiosResult.data
}