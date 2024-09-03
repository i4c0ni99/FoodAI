import { IODiet } from "../page/chatAI.page"




export const Daily_diet: React.FC<IODiet> = ({ meal }) => {
    
    console.log('ciao')
    console.log(meal)
    return (<>
        {meal && 
            (<>
            
                <div className="stats bg-primary text-primary-content">
                    <div className="stat">
                    <h1 className=" mb-2 ml-6">{meal.carbohydrate.description}</h1>
                        <div className="stats shadow">
                            <div className="stat">
                                <div className="stat-title">Carbs</div>
                                <div className="stat-value">{meal.carbohydrate.carbohydrate.toFixed(2)} g</div>
                            </div>

                            <div className="stat">
                                <div className="stat-title">Proteins</div>
                                <div className="stat-value">{meal.carbohydrate.protein.toFixed(2)} g</div>
                            </div>

                            <div className="stat">
                                <div className="stat-title">Fat</div>
                                <div className="stat-value">{meal.carbohydrate.fat.toFixed(2)} g</div>
                            </div>
                        </div>
                    </div>

                    <div className="stat">
                        <div className="stat-title">Total Kalories</div>
                        <div className="stat-value">{meal.carbohydrate.kilocalories.toFixed(2)}K</div>
                        <div className="stat-title">Total Grams</div>
                        <div className="stat-value">{meal.carbohydrate.grams.toFixed(2)}G</div>
                        <div className="stat-actions">
                            <button className="btn btn-sm">Like</button>
                            <button className="btn btn-sm ml-2">Dislike</button>
                        </div>
                    </div>
                </div>
                <div className="stats bg-primary text-primary-content my-4">
                    <div className="stat">
                    <h1 className=" mb-2 ml-6">{meal.protein.description}</h1>
                        <div className="stats shadow">
                            <div className="stat">
                                <div className="stat-title">Carbs</div>
                                <div className="stat-value">{meal.protein.carbohydrate.toFixed(2)} g</div>
                            </div>

                            <div className="stat">
                                <div className="stat-title">Proteins</div>
                                <div className="stat-value">{meal.protein.protein.toFixed(2)} g</div>
                            </div>

                            <div className="stat">
                                <div className="stat-title">Fat</div>
                                <div className="stat-value">{meal.protein.fat.toFixed(2)} g</div>
                            </div>
                        </div>
                    </div>

                    <div className="stat">
                        <div className="stat-title">Total Kalories</div>
                        <div className="stat-value">{meal.protein.kilocalories.toFixed(2)}K</div>
                        <div className="stat-title">Total Grams</div>
                        <div className="stat-value">{meal.protein.grams.toFixed(2)}G</div>
                        <div className="stat-actions">
                            <button className="btn btn-sm">Like</button>
                            <button className="btn btn-sm ml-2">Dislike</button>
                        </div>
                    </div>
                </div>
                <div className="stats bg-primary text-primary-content">
                    <div className="stat">
                    <h1 className=" mb-2 ml-6">{meal.fat.description}</h1>
                        <div className="stats shadow">
                            <div className="stat">
                                <div className="stat-title">Carbs</div>
                                <div className="stat-value">{meal.fat.carbohydrate.toFixed(2)} g</div>
                            </div>

                            <div className="stat">
                                <div className="stat-title">Proteins</div>
                                <div className="stat-value">{meal.fat.protein.toFixed(2)} g</div>
                            </div>

                            <div className="stat">
                                <div className="stat-title">Fat</div>
                                <div className="stat-value">{meal.fat.fat.toFixed(2)} g</div>
                            </div>
                        </div>
                    </div>

                    <div className="stat">
                        <div className="stat-title">Total Kalories</div>
                        <div className="stat-value">{meal.fat.kilocalories.toFixed(2)}K</div>
                        <div className="stat-title">Total Grams</div>
                        <div className="stat-value">{meal.fat.grams.toFixed(2)}G</div>
                        <div className="stat-actions">
                            <button className="btn btn-sm">Like</button>
                            <button className="btn btn-sm ml-2">Dislike</button>
                        </div>
                    </div>
                </div>
              
            </> 
            )}


    </>)
}