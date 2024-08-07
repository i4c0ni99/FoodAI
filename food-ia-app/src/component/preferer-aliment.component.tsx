import { ChangeEvent, useState } from "react"

interface IChoicheCard {
    aliment: {
        name: string,
        category: string,
        img: string,
        checked: boolean
    }
    onSubmission?: (data: boolean) => void;
}

export const ChoichePrefAliment: React.FC<IChoicheCard> = ({ aliment,onSubmission }) => {
    const [checked, setChecked] = useState(false)
    const handleCheckboxChange = () => {
        setChecked(!checked)
        if(onSubmission)
        onSubmission(!checked)
    }

    return (<>
        <div className={`card transition-opacity cursor-pointer ${checked ? 'bg-base-300 opacity-50' : 'bg-base-300 opacity-100'}`} onClick={handleCheckboxChange}>
            <div className="card bg-base-100 w-96 shadow-xl ">
                
                <figure>
                <input type="checkbox" name={aliment.category} id={aliment.category}
                        checked={checked}
                        onChange={handleCheckboxChange}
                        className="hidden" />
                    <img
                        src={aliment.img}
                        alt="" />
                </figure>
                <div className="card-body">
                    <h2 className="card-title">{aliment.name}</h2>
                </div>
            </div>
        </div>
    </>)
}