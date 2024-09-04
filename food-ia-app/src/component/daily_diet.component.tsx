import { useState } from "react"
import { IODiet } from "../page/chatAI.page"
import { axiosInstance } from "../utils/axoisInstance.utils"
import { getCookie } from "../utils/cookies.service"





export const Daily_diet: React.FC<IODiet> = ({ meal, type }) => {
    const allData = getCookie('calMacro&aliments')
    const [food, setFood] = useState<IODiet>( {meal,type})
    async function dislikeCarbs() {
        try{
            const axiosResult = await axiosInstance.post('/changeAliment/', {
                'aliments': allData.aliments,
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
                'assignment': { 'protein': meal.protein, 'fat': meal.fat }

            });

            // Controllo della validità dei dati ricevuti
            /* console.log(axiosResult.data)
            console.log("Dati ricevuti:", axiosResult.data); */

            // Assicurati che i dati siano assegnati correttamente
            const food_changed: IODiet = { meal: axiosResult.data.meal, type: type };
            //console.log("Dati che verranno settati in state:", food_changed);
    
            setFood(food_changed); // Imposta lo stato
        } catch (error) {
            console.error("Error fetching data from API:", error);
        }
        
        
    }
    async function dislikeProtein() {
        try {
            const axiosResult = await axiosInstance.post('/changeAliment/', {
                'aliments': allData.aliments,
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
                'assignment': { 'carbohydrate': meal.carbohydrate, 'fat': meal.fat }

            });

            // Controllo della validità dei dati ricevuti
            /* console.log(axiosResult.data)
            console.log("Dati ricevuti:", axiosResult.data); */

            // Assicurati che i dati siano assegnati correttamente
            const food_changed: IODiet = { meal: axiosResult.data.meal, type: type };
            //console.log("Dati che verranno settati in state:", food_changed);
    
            setFood(food_changed); // Imposta lo stato
        } catch (error) {
            console.error("Error fetching data from API:", error);
        }
        
    }
    async function dislikeFat() {
        try {
            const axiosResult = await axiosInstance.post('/changeAliment/', {
                'aliments': allData.aliments,
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
                'assignment': { 'protein': meal.protein, 'carbohydrate': meal.carbohydrate }

            });

            // Controllo della validità dei dati ricevuti
            /* console.log(axiosResult.data)
            console.log("Dati ricevuti:", axiosResult.data); */

            // Assicurati che i dati siano assegnati correttamente
            const food_changed: IODiet = { meal: axiosResult.data.meal, type: type };
            //console.log("Dati che verranno settati in state:", food_changed);
    
            setFood(food_changed); // Imposta lo stato
        } catch (error) {
            console.error("Error fetching data from API:", error);
        }
    }



return (<>
{console.log(food)}
    {food.meal.carbohydrate && food.meal.protein && food.meal.fat &&
        (<>

            <div className="stats bg-primary text-primary-content">
                <div className="stat">
                    <h1 className=" mb-2 ml-6" >{food.meal.carbohydrate.description}</h1>
                    <div className="stats shadow">
                        <div className="stat">
                            <div className="stat-title">Carbs</div>
                            <div className="stat-value">{food.meal.carbohydrate.carbohydrate.toFixed(2)} g</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Proteins</div>
                            <div className="stat-value">{food.meal.carbohydrate.protein.toFixed(2)} g</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Fat</div>
                            <div className="stat-value">{food.meal.carbohydrate.fat.toFixed(2)} g</div>
                        </div>
                    </div>
                </div>

                <div className="stat">
                    <div className="stat-title">Total Kalories</div>
                    <div className="stat-value">{food.meal.carbohydrate.kilocalories.toFixed(2)}K</div>
                    <div className="stat-title">Total Grams</div>
                    <div className="stat-value">{food.meal.carbohydrate.grams.toFixed(2)}G</div>
                    <div className="stat-actions">
                        <button className="btn btn-sm ml-2" onClick={dislikeCarbs}>Dislike</button>
                    </div>
                </div>
            </div>
            <div className="stats bg-primary text-primary-content my-4">
                <div className="stat">
                    <h1 className=" mb-2 ml-6">{food.meal.protein.description}</h1>
                    <div className="stats shadow">
                        <div className="stat">
                            <div className="stat-title">Carbs</div>
                            <div className="stat-value">{food.meal.protein.carbohydrate.toFixed(2)} g</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Proteins</div>
                            <div className="stat-value">{food.meal.protein.protein.toFixed(2)} g</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Fat</div>
                            <div className="stat-value">{food.meal.protein.fat.toFixed(2)} g</div>
                        </div>
                    </div>
                </div>

                <div className="stat">
                    <div className="stat-title">Total Kalories</div>
                    <div className="stat-value">{food.meal.protein.kilocalories.toFixed(2)}K</div>
                    <div className="stat-title">Total Grams</div>
                    <div className="stat-value">{food.meal.protein.grams.toFixed(2)}G</div>
                    <div className="stat-actions">
                        <button className="btn btn-sm ml-2" onClick={dislikeProtein}>Dislike</button>
                    </div>
                </div>
            </div>
            <div className="stats bg-primary text-primary-content">
                <div className="stat">
                    <h1 className=" mb-2 ml-6">{food.meal.fat.description}</h1>
                    <div className="stats shadow">
                        <div className="stat">
                            <div className="stat-title">Carbs</div>
                            <div className="stat-value">{food.meal.fat.carbohydrate.toFixed(2)} g</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Proteins</div>
                            <div className="stat-value">{food.meal.fat.protein.toFixed(2)} g</div>
                        </div>

                        <div className="stat">
                            <div className="stat-title">Fat</div>
                            <div className="stat-value">{food.meal.fat.fat.toFixed(2)} g</div>
                        </div>
                    </div>
                </div>

                <div className="stat">
                    <div className="stat-title">Total Kalories</div>
                    <div className="stat-value">{food.meal.fat.kilocalories.toFixed(2)}K</div>
                    <div className="stat-title">Total Grams</div>
                    <div className="stat-value">{food.meal.fat.grams.toFixed(2)}G</div>
                    <div className="stat-actions">
                        <button className="btn btn-sm ml-2" onClick={dislikeFat}>Dislike</button>
                    </div>
                </div>
            </div>

        </>
        )}


</>)
}
