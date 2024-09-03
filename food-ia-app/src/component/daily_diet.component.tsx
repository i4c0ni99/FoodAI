import { IODiet } from "../page/chatAI.page"




export const Daily_diet: React.FC<IODiet> = ({ meal }) => {
    
    console.log('ciao')
    console.log(meal)
    return (<>
        {meal &&
            (
                <div className="stats bg-primary text-primary-content">
                    <div className="stat">
                    <h1 className=" mb-2 ml-6">{meal.carbohydrate.description}</h1>
                        <div className="stats shadow">
                            <div className="stat">
                                <div className="stat-figure text-secondary">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        className="inline-block h-8 w-8 stroke-current">
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                </div>
                                <div className="stat-title">Carbs</div>
                                <div className="stat-value">31K</div>
                                <div className="stat-desc">Jan 1st - Feb 1st</div>
                            </div>

                            <div className="stat">
                                <div className="stat-figure text-secondary">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        className="inline-block h-8 w-8 stroke-current">
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path>
                                    </svg>
                                </div>
                                <div className="stat-title">New Users</div>
                                <div className="stat-value">4,200</div>
                                <div className="stat-desc">↗︎ 400 (22%)</div>
                            </div>

                            <div className="stat">
                                <div className="stat-figure text-secondary">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        className="inline-block h-8 w-8 stroke-current">
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path>
                                    </svg>
                                </div>
                                <div className="stat-title">New Registers</div>
                                <div className="stat-value">1,200</div>
                                <div className="stat-desc">↘︎ 90 (14%)</div>
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
            )}


    </>)
}