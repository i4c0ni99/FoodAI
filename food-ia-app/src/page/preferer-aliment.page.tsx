import { useEffect, useState } from "react"
import { ChoichePrefAliment } from "../component/preferer-aliment.component"
import { getAlimentMock } from "../mock/getAliment.mock"
import { axiosInstance } from "../utils/axoisInstance.utils"
import { getCookie, setDietCookie, setUserCookie } from "../utils/cookies.service"



export const PrefererAliment = ({
}) => {
    const [aliments, setAliments] = useState<{ name: string, category: string, img: string, checked: boolean }[]>([])
    const [showAlert, setShowAlert] = useState(false);

    const onSubmit=async ()=>{
       const alimentsTrue = aliments.filter((alimentTrue) => alimentTrue.checked)
       if(alimentsTrue.length >= 4 ){
       const allData =  getCookie('calMacro&aliments')
       setShowAlert(false)
       console.log(allData,alimentsTrue)
        const axiosResult= await axiosInstance.post('/colazione/',
        {
            'aliments':alimentsTrue,
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena':allData.cena,
            'colazione':allData.colazione,
            'pranzo':allData.pranzo,
            'spuntino_mat':allData.spuntino_mat,
            'spuntino_pom':allData.spuntino_pom,
            'meal' : '',
            'assignment': {}
        }
        
       )
        setUserCookie({
            'aliments':alimentsTrue,
            'tdee': allData.tdee,
            'carb_g': allData.carb_g,
            'protein_g': allData.protein_g,
            'fat_g': allData.fat_g,
            'cena':allData.cena,
            'colazione':allData.colazione,
            'pranzo':allData.pranzo,
            'spuntino_mat':allData.spuntino_mat,
            'spuntino_pom':allData.spuntino_pom,
            'meal' : '',
            'assignment': {}
        })
        
        setDietCookie(axiosResult.data)
        window.location.href= "/chat"
       }else setShowAlert(true)
    }
    useEffect(() => {
        const fetchData = async () => {
            const aliments = await getAlimentMock()
            setAliments(aliments)
        }

        fetchData()
    }, [])
    return (
        <>
        {showAlert &&(
            <div role="alert" className="alert alert-error fixed z-50">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6 shrink-0 stroke-current"
              fill="none"
              viewBox="0 0 24 24">
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>Numero di alimenti troppo basso per creare una dieta!!!!</span>
          </div>
      )}
        <main className="pt-32 pl-2 pr-2 sm:size-11/12 lg:size-4/5 mx-auto">
            <div className="card bg-base-300 size full shadow-xl">
                <div className="card-body items-center text-center">
                    <h2 className="card-title text-xl font-medium">Alimenti!</h2>
                    <p className="text-l font-medium">Scegli i cib i che desideri mangiare oggi </p>
                </div>
                <div className="flex flex-auto gap-4 flex-wrap place-content-center pt-32">

                    {aliments.map((aliment) => (
                        <ChoichePrefAliment aliment={aliment} onSubmission={(check: boolean) => {
                            aliment.checked = check
                            console.log(aliment.checked)
                        }
                        }></ChoichePrefAliment>
                    )
                    )}
                </div>
                <button className="btn btn-accent" onClick={onSubmit}>Conferma</button>
            </div>
            
        </main>

        </>

    )
}