
import { Daily_diet } from "../component/daily_diet.component"
import { getCookie } from "../utils/cookies.service"

export interface fat {
    fat: {
        aliment:

        [{
            original_category: string, category: string, description: string,
            carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string
        }]
        , grams: number
    }
}
export interface protein {
    protein: {
        aliment:

        [{
            original_category: string, category: string, description: string,
            carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string
        }]
        , grams: number
    }
}
export interface carbs {
    carbohydrate: {
        aliment:

        [{
            original_category: string, category: string, description: string,
            carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string
        }]
        , grams: number
    }
}
export interface IODiet {
    pranzo: {
        carbohydrate: {
            aliment:

            [{
                original_category: string, category: string, description: string,
                carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string
            }]
            , grams: number
        },
        protein: {
            aliment:

            [{
                original_category: string, category: string, description: string,
                carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string
            }]
            , grams: number
        }, 
        fat: {
            aliment:

            [{
                original_category: string, category: string, description: string,
                carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string
            }]
            , grams: number
        }


    }

}

export function ChatIA() {
    const allData: [IODiet] = getCookie('daily_diet')
    //console.log(allData[0]['pranzo'])

    return (
        <>
            <div className=" grid justify-items-center w-screen">
                <h1 className="text-5xl font-bold mt-8 ">Daily diet!</h1>
            </div>
            <main className="pt-24 pl-2 pr-2 sm:size-11/12 lg:size-4/5 mx-auto">

                <div className="card bg-base-200 size full shadow-xl grid justify-items-center pb-8">
                    <h1 className="text-2xl font-bold my-4  ">Launch!</h1>
                    {allData && allData.map((meal: IODiet) => {
                        if (meal['pranzo']) {
                            console.log(meal['pranzo'])
                            return <Daily_diet pranzo={meal['pranzo']} ></Daily_diet>
                        }
                        else return <span className="loading loading-spinner loading-lg"></span>
                    })}
                </div>
            </main>

        </>
    )
}