import { ChangeEvent, FormEvent, useState } from "react";

interface Data {
    eta: number,
    altezza: number,
    peso: number
    obbiettivo:string,
    stile_di_vita:string,
    numero_di_pasti:number
}

interface ICalc {

    onSubmission?: (data: Data) => void;
}


export const KalMacroCalculator: React.FC<ICalc> = ({ onSubmission }) => {
    const [data, setData] = useState<Data>({ eta: 0, altezza: 0, peso: 0 ,obbiettivo:'',stile_di_vita:'',numero_di_pasti : 5})
    const onSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        if (onSubmission)
            onSubmission(data)
    }

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.value)
            console.log(e.target.value)
            setData((prev) => ({

                ...prev,
                [e.target.name]:  e.target.value
            })
            )
    }

    return (<>

        <div className="hero bg-base-300 min-h-screen px-8 py-8">
            <div className="hero-content flex-col lg:flex-row-reverse">
                <div className="text-center lg:text-left">
                    <h1 className="text-5xl font-bold">Calcola ora!</h1>
                    <p className="py-6">
                        Calcola ora le tue kalorie giornaliere e macro che ti permetteranno di raggiungere i tuoi obbiettivi
                    </p>
                    <h1 className="text-3xl font-bold">Seleziona obbiettivo e stile di vita!</h1>
                    <div className=" mt-2 flex w-1/2">
                        <input type="radio" name="obbiettivo" aria-label="Dimagrimento" value="dimagrimento" onChange={handleChange} className="btn glass h-16 basis-3/4" />
                        <div className="avatar basis-1/4">
                            <div className="w-16 rounded ">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                        <input type="radio" name="stile_di_vita" aria-label="Sedentario" value="sedentario" onChange={handleChange} className="btn glass h-16 basis-3/4 ml-2" />
                        <div className="avatar basis-1/4">
                            <div className="w-16 rounded">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                    </div>
                    <div className=" mt-2 flex w-1/2">
                        <input type="radio" name="obbiettivo" aria-label="Mantenimento" value="mantenimento" onChange={handleChange} className="btn glass h-16 basis-3/4" />
                        <div className="avatar basis-1/4">
                            <div className="w-16 rounded">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                        <input type="radio" name="stile_di_vita" aria-label="Attivo" value="attivo" onChange={handleChange} className="btn glass h-16 basis-3/4 ml-2" />
                        <div className="avatar basis-1/4">
                            <div className="w-16 rounded">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                    </div>
                    <div className=" mt-2 flex w-1/2">
                        <input type="radio" name="obbiettivo" aria-label="Massa" value="massa" onChange={handleChange} className="btn glass h-16 basis-3/4" />
                        <div className="avatar basis-1/4">
                            <div className="w-16 rounded">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                        <input type="radio" name="stile_di_vita" aria-label="Molto attivo" value="molto attivo" onChange={handleChange} className="btn glass h-16 basis-3/4 ml-2" />
                        <div className="avatar basis-1/4">
                            <div className="w-16 rounded">
                                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                    </div>
                </div>
                <div className="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
                    <form className="card-body" onSubmit={onSubmit}>
                        <div className="form-control">
                            <label className="label">
                                <span className="label-text">Età</span>
                            </label>
                            <input type="text" onChange={handleChange} placeholder="età" name="eta" className="input input-bordered" required />
                        </div>
                        <div className="form-control">
                            <label className="label">
                                <span className="label-text">Altezza</span>
                            </label>
                            <input type="text" onChange={handleChange} placeholder="Altezza" name="altezza" className="input input-bordered" required />
                        </div>
                        <div className="form-control">
                            <label className="label">
                                <span className="label-text">Peso</span>
                            </label>
                            <input type="text" onChange={handleChange} placeholder="Peso" name='peso'className="input input-bordered" required />
                        </div>
                        <div className="form-control mt-6">
                            <button className="btn btn-accent">Calcola</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </>)
}