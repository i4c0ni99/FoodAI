import { useEffect, useState } from "react";
import { Daily_diet } from "../component/daily_diet.component";
import { getCookie } from "../utils/cookies.service";
import {
    serverRequestCena,
    serverRequestPranzo,
    serverRequestSpuntino_mat,
    serverRequestSpuntino_pom
} from "../utils/request.server";

export interface IODiet {
    meal: {
        carbohydrate: {
            category: string;
            description: string;
            carbohydrate: number;
            protein: number;
            fat: number;
            kilocalories: number;
            generic_category: string;
            grams: number;
        },
        protein: {
            category: string;
            description: string;
            carbohydrate: number;
            protein: number;
            fat: number;
            kilocalories: number;
            generic_category: string;
            grams: number;
        },
        fat: {
            category: string;
            description: string;
            carbohydrate: number;
            protein: number;
            fat: number;
            kilocalories: number;
            generic_category: string;
            grams: number;
        }
    },type : string

}

export function ChatIA() {
    const [colazione, setColazione] = useState<IODiet>();
    const [spuntino_mat, setSpuntino_mat] = useState<IODiet>();
    const [pranzo, setPranzo] = useState<IODiet>();
    const [spuntino_pom, setSpuntino_pom] = useState<IODiet>();
    const [cena, setCena] = useState<IODiet>();
    const totalCarb = totalCarbs()
    const totalKal = kilototal()
    const totalProt = totalProts()
    const totalFat =  totalFats()
    const userData = getCookie('calMacro&aliments')
    function totalCarbs(){
        if(colazione && spuntino_mat && pranzo && spuntino_pom && cena){
            const  totalKal : number = colazione.meal.carbohydrate.carbohydrate + colazione.meal.protein.carbohydrate + colazione.meal.fat.carbohydrate +
            spuntino_mat.meal.carbohydrate.carbohydrate + spuntino_mat.meal.fat.carbohydrate + spuntino_mat.meal.protein.carbohydrate +
            pranzo.meal.carbohydrate.carbohydrate + pranzo.meal.fat.carbohydrate + pranzo.meal.protein.carbohydrate +
            spuntino_pom.meal.carbohydrate.carbohydrate +spuntino_pom.meal.fat.carbohydrate +spuntino_pom.meal.protein.carbohydrate +
            cena.meal.carbohydrate.carbohydrate +cena.meal.fat.carbohydrate + cena.meal.protein.carbohydrate 
            return totalKal.toFixed(2)
        }
    }
    function totalProts(){
        if(colazione && spuntino_mat && pranzo && spuntino_pom && cena){
            const  totalKal : number = colazione.meal.carbohydrate.protein + colazione.meal.protein.protein + colazione.meal.fat.protein +
            spuntino_mat.meal.carbohydrate.protein + spuntino_mat.meal.fat.protein + spuntino_mat.meal.protein.protein +
            pranzo.meal.carbohydrate.protein + pranzo.meal.fat.protein + pranzo.meal.protein.protein +
            spuntino_pom.meal.carbohydrate.protein +spuntino_pom.meal.fat.protein +spuntino_pom.meal.protein.protein +
            cena.meal.carbohydrate.protein +cena.meal.fat.protein + cena.meal.protein.protein 
            return totalKal.toFixed(2)
        }
    }
    function totalFats(){
        if(colazione && spuntino_mat && pranzo && spuntino_pom && cena){
            const  totalKal : number = colazione.meal.carbohydrate.fat + colazione.meal.protein.fat + colazione.meal.fat.fat +
            spuntino_mat.meal.carbohydrate.fat + spuntino_mat.meal.fat.fat + spuntino_mat.meal.protein.fat +
            pranzo.meal.carbohydrate.fat + pranzo.meal.fat.fat + pranzo.meal.protein.fat +
            spuntino_pom.meal.carbohydrate.fat +spuntino_pom.meal.fat.fat +spuntino_pom.meal.protein.fat +
            cena.meal.carbohydrate.fat +cena.meal.fat.fat + cena.meal.protein.fat 
            return totalKal.toFixed(2)
        }
    }

   
    function kilototal(){
        if(colazione && spuntino_mat && pranzo && spuntino_pom && cena){
            return (colazione.meal.carbohydrate.kilocalories + colazione.meal.fat.kilocalories + colazione.meal.protein.kilocalories +
            spuntino_mat.meal.carbohydrate.kilocalories + spuntino_mat.meal.fat.kilocalories + spuntino_mat.meal.protein.kilocalories +
            pranzo.meal.carbohydrate.kilocalories + pranzo.meal.fat.kilocalories + pranzo.meal.protein.kilocalories +
            spuntino_pom.meal.carbohydrate.kilocalories +spuntino_pom.meal.fat.kilocalories +spuntino_pom.meal.protein.kilocalories +
            cena.meal.carbohydrate.kilocalories +cena.meal.fat.kilocalories + cena.meal.protein.kilocalories ).toFixed(2)
            
        }
       
            
        }   

  
   
    const [iterator,setIterator]= useState<number>(0)
    useEffect(() => {
        async function fetchData() {
            try {
                
                const colazione: IODiet = await getCookie('daily_diet')
                
                
                const spuntinoMatData = await serverRequestSpuntino_mat();
               
    
                const pranzoData = await serverRequestPranzo();
                
    
                const spuntinoPomData = await serverRequestSpuntino_pom();
                
    
                const cenaData = await serverRequestCena();
                
            const totalKal = colazione.meal.carbohydrate.kilocalories + colazione.meal.fat.kilocalories + colazione.meal.protein.kilocalories +
            spuntinoMatData.data.meal.carbohydrate.kilocalories + spuntinoMatData.data.meal.fat.kilocalories + spuntinoMatData.data.meal.protein.kilocalories +
            pranzoData.data.meal.carbohydrate.kilocalories + pranzoData.data.meal.fat.kilocalories + pranzoData.data.meal.protein.kilocalories +
            spuntinoPomData.data.meal.carbohydrate.kilocalories +spuntinoPomData.data.meal.fat.kilocalories +spuntinoPomData.data.meal.protein.kilocalories +
            cenaData.data.meal.carbohydrate.kilocalories +cenaData.data.meal.fat.kilocalories + cenaData.data.meal.protein.kilocalories 
            console.log(totalKal)
            if(totalKal && Math.abs(parseFloat(totalKal)  - userData['tdee']) <=  parseFloat(totalKal) * 0.025 ){
                    console.log('entrato')
                    setColazione(colazione) 
                    setSpuntino_mat(spuntinoMatData.data);
                    setPranzo(pranzoData.data);
                    setSpuntino_pom(spuntinoPomData.data);
                    setCena(cenaData.data);
               }
               else setIterator(iterator + 1)
                
                
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }

        fetchData();
    }, [iterator]); // Dipendenze vuote per evitare richieste infinite
    return (
        <>
        {/* 'aliments': allData.aliments,
                'tdee': allData.tdee,
                'carb_g': allData.carb_g,
                'protein_g': allData.protein_g,
                'fat_g': allData.fat_g,
                'cena': allData.cena,
                'colazione': allData.colazione,
                'pranzo': allData.pranzo,
                'spuntino_mat': allData.spuntino_mat,
                'spuntino_pom': allData.spuntino_pom,
                'meal': type,
                'assignment': { 'protein': meal.protein, 'fat': meal.fat  */}
            <div className="grid justify-items-center w-screen">
                <h1 className="text-5xl font-bold mt-8">Daily diet!</h1>
            </div>
            <main className="pt-24 pl-2 pr-2 sm:size-11/12 lg:size-4/5 mx-auto">
            <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8 ">
                    <h1 className="text-2xl font-bold my-4">Tutta la tua giornata!</h1>
                    <div className="stats bg-secondary text-primary-content">
                <div className="stat">
                    <h1 className=" mb-2 ml-6" >Kalorie e macro da assumere</h1>
                    <div className="stats shadow">
                        <div className="stat">
                            <div className="stat-title">Carbs</div>
                            <div className="stat-value">{userData['carb_g'].toFixed(2)} g</div>
                            <div className="stat-desc">{totalCarb}</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Proteins</div>
                            <div className="stat-value">{userData['protein_g'].toFixed(2)} g</div>
                            <div className="stat-desc">{totalProt}</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Fat</div>
                            <div className="stat-value">{userData['fat_g'].toFixed(2)} g</div>
                            <div className="stat-desc">{totalFat}</div>
                        </div>
                    </div>
                </div>

                <div className="stat">
                    <div className="stat-title">Total Kalories</div>
                    <div className="stat-value">{totalKal} K /</div>
                    <div className="stat-title">target Kalories</div>
                    <div className="stat-value">{userData['tdee'].toFixed(2)}</div>
                </div>
            </div>
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8 ">
                    <h1 className="text-2xl font-bold my-4">Colazione!</h1>
                    {!colazione && (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                    {colazione && (<Daily_diet meal={colazione.meal} type={"colazione"} />)}
                </div>

                {/*  {/* Abilita questi elementi quando vuoi testarli */}
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Spuntino mattutino!</h1>
                    {spuntino_mat ? (
                        <Daily_diet meal={spuntino_mat.meal} type={"spuntino_mat"} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Pranzo!</h1>
                    {pranzo ? (
                        <Daily_diet meal={pranzo.meal} type={"pranzo"} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Spuntino pomeridiano!</h1>
                    {spuntino_pom ? (
                        <Daily_diet meal={spuntino_pom.meal} type={"spuntino_pom"} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Cena!</h1>
                    {cena ? (
                        <Daily_diet meal={cena.meal} type={"cena"} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
            </main>
        </>
    );
}
