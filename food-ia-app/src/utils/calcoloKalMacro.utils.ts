
interface Data {
    eta: number,
    altezza: number,
    peso: number
    obbiettivo:string,
    stile_di_vita:string,
    numero_di_pasti: number
}

interface KalPerPasto {
    colazione :number,
    spuntino_mat:number,
    pranzo : number,
    spuntino_pom : number,
    cena :number
}


export function calculateKalMacro(data:Data): { tdee:number,protein_g:number, carb_g:number,fat_g:number, pasti: KalPerPasto }{
    let activity_factor: number;

    switch (data.stile_di_vita) {
        case 'sedentario':
            activity_factor = 1.0;
            break;
        case 'attivo':
            activity_factor = 1.55;
            break;
        case 'molto attivo':
            activity_factor = 1.75;
            break;
        default:
            throw new Error("Livello di attività non valido");
    }

    const bmr = 10 * data.peso + 6.25 * data.altezza - 5  * data.eta + 5;
    let tdee : number = bmr * activity_factor;
    const macro= calculateMacronutrientPercentages(data.stile_di_vita,tdee,data.obbiettivo)
    const carb_g =macro.carb_g
    const protein_g= macro.protein_g
    const fat_g = macro.fat_g
    tdee = macro.tdee
    let spuntino_mat:number
    let colazione :number
    let pranzo : number
    let spuntino_pom : number
    let cena :number
    switch(data.numero_di_pasti){
        case 5:
         colazione = tdee * 0.20
         spuntino_mat = tdee * 0.07
         pranzo= tdee * 0.35
         spuntino_pom = tdee * 0.08
         cena = tdee * 0.30
         break
        default:
            throw new Error("numero pasti non consentito");  
    }
   const pasti : KalPerPasto = {colazione,spuntino_mat,pranzo,spuntino_pom,cena}
    
    return {tdee,protein_g,carb_g,fat_g,pasti}
}


function calculateMacronutrientPercentages(stile_di_vita:string,tdee: number, goal: string): {tdee:number, protein_g: number, carb_g: number, fat_g: number } {
    let protein_percentage: number;
    let carb_percentage: number;
    let fat_percentage: number;

    switch (goal) {
        case 'dimagrimento':
            switch (stile_di_vita) {
                case 'sedentario':
                    carb_percentage = 0.3;
                    protein_percentage = 0.4;
                    fat_percentage = 0.3;
                    break;
                case 'attivo':
                    carb_percentage = 0.35;
                    protein_percentage = 0.4;
                    fat_percentage = 0.25;
                    break;
                case 'molto attivo':
                    carb_percentage = 0.40;
                    protein_percentage = 0.35;
                    fat_percentage = 0.25;
                    break;
                default:
                    throw new Error("Livello di attività non valido");
            }
            tdee -=500
           break
        case 'mantenimento':
            switch (stile_di_vita) {
                case 'sedentario':
                    carb_percentage = 0.45;
                    protein_percentage = 0.30;
                    fat_percentage = 0.20;
                    break;
                case 'attivo':
                    carb_percentage = 0.50;
                    protein_percentage = 0.25;
                    fat_percentage = 0.25;
                    break;
                case 'molto attivo':
                    carb_percentage = 0.50;
                    protein_percentage = 0.25;
                    fat_percentage = 0.25;
                    break;
                default:
                    throw new Error("Livello di attività non valido");
            }
            break;
        case 'massa':
            tdee +=500
            switch (stile_di_vita) {
                case 'sedentario':
                    carb_percentage = 0.5;
                    protein_percentage = 0.3;
                    fat_percentage = 0.2;
                    break;
                case 'attivo':
                    carb_percentage = 0.55;
                    protein_percentage = 0.30;
                    fat_percentage = 0.15;
                    break;
                case 'molto attivo':
                    carb_percentage = 0.55;
                    protein_percentage = 0.30;
                    fat_percentage = 0.15;
                    break;
                default:
                    throw new Error("Livello di attività non valido");
            }
            break;
        default:
            throw new Error("Obiettivo non valido");
    }

    const protein_g = protein_percentage * tdee / 4;
    const carb_g = carb_percentage * tdee / 4;
    const fat_g = fat_percentage * tdee / 9;
     
    
    return { tdee,protein_g, carb_g, fat_g };
}