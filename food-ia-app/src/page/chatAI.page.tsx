import { useEffect, useState } from "react";
import { Daily_diet } from "../component/daily_diet.component";
import { getCookie } from "../utils/cookies.service";
import {
    serverRequestCena,
    serverRequestPranzo,
    serverRequestSpuntino_mat
} from "../utils/request.server";

export interface IODiet {
    meal: {
        carbohydrate: {
            original_category: string;
            category: string;
            description: string;
            carbohydrate: number;
            protein: number;
            fat: number;
            kilocalories: number;
            feedback: string;
            generic_category: string;
            grams: number;
        },
        protein: {
            original_category: string;
            category: string;
            description: string;
            carbohydrate: number;
            protein: number;
            fat: number;
            kilocalories: number;
            feedback: string;
            generic_category: string;
            grams: number;
        },
        fat: {
            original_category: string;
            category: string;
            description: string;
            carbohydrate: number;
            protein: number;
            fat: number;
            kilocalories: number;
            feedback: string;
            generic_category: string;
            grams: number;
        }
    }

}

export function ChatIA() {
    const [colazione, setColazione] = useState<IODiet>();
    const [spuntino_mat, setSpuntino_mat] = useState<IODiet>();
    const [pranzo, setPranzo] = useState<IODiet>();
    const [spuntino_pom, setSpuntino_pom] = useState<IODiet>();
    const [cena, setCena] = useState<IODiet>();

    useEffect(() => {
        async function fetchData() {
            try {
                const colazione: IODiet = await getCookie('daily_diet')
                setColazione(colazione)
                console.log('ciaooooooo')
                const spuntinoMatData = await serverRequestSpuntino_mat();
                console.log(spuntinoMatData)
                setSpuntino_mat(spuntinoMatData.data);

                const pranzoData = await serverRequestPranzo();
                setPranzo(pranzoData);

                const spuntinoPomData = await serverRequestSpuntino_mat();
                setSpuntino_pom(spuntinoPomData.data);

                const cenaData = await serverRequestCena();
                setCena(cenaData);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }

        fetchData();
    }, []); // Dipendenze vuote per evitare richieste infinite
    console.log('colazione',colazione)
  console.log('spuntino mat',spuntino_mat)
  console.log('pranzo ',pranzo)
  console.log('spuntino pom',spuntino_pom)
  console.log('cena',cena)
    return (
        <>
            <div className="grid justify-items-center w-screen">
                <h1 className="text-5xl font-bold mt-8">Daily diet!</h1>
            </div>
            <main className="pt-24 pl-2 pr-2 sm:size-11/12 lg:size-4/5 mx-auto">
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8 ">
                    <h1 className="text-2xl font-bold my-4">Colazione!</h1>
                    {!colazione && (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                    {colazione && (<Daily_diet meal={colazione.meal} />)}
                </div>

                {/*  {/* Abilita questi elementi quando vuoi testarli */}
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Spuntino mattutino!</h1>
                    {spuntino_mat ? (
                        <Daily_diet meal={spuntino_mat.meal} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Pranzo!</h1>
                    {pranzo ? (
                        <Daily_diet meal={pranzo.meal} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Spuntino pomeridiano!</h1>
                    {spuntino_pom ? (
                        <Daily_diet meal={spuntino_pom.meal} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4">Cena!</h1>
                    {cena ? (
                        <Daily_diet meal={cena.meal} />
                    ) : (
                        <span className="loading loading-spinner loading-lg"></span>
                    )}
                </div>
            </main>
        </>
    );
}
