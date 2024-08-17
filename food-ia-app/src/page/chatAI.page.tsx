
import { Daily_diet } from "../component/daily_diet.component"
import { getCookie } from "../utils/cookies.service"



export interface IODiet {
    meal: { pranzo:
         { carbs:
             { aliment: 
                [{ original_category: string, category: string, description: string, 
                    carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string }]
                    , grams: number } 
                } }
}

export function ChatIA() {
    const allData : IODiet[] = getCookie('daily_diet')
    console.log(allData)

    return (
        <>
            <div className=" grid justify-items-center w-screen">
                <h1 className="text-5xl font-bold mt-8 ">Daily diet!</h1>
            </div>
            <main className="pt-24 pl-2 pr-2 sm:size-11/12 lg:size-4/5 mx-auto">

                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4  ">Launch!</h1>
                   


                </div>
            </main>

        </>
    )
}