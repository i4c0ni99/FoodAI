import { Link } from "react-router-dom"

export const CopertineComp =({})=>{
    return (<>
    <div
  className="hero min-h-screen"
  style={{
    backgroundImage: "url(https://images.theconversation.com/files/158563/original/image-20170227-26322-nl8u98.jpg?ixlib=rb-4.1.0&q=20&auto=format&w=320&fit=clip&dpr=2&usm=12&cs=strip)",
  }}>
  <div className="hero-overlay bg-opacity-60"></div>
  <div className="hero-content text-neutral-content text-center">
    <div className="max-w-md">
      <h1 className="mb-5 text-5xl font-bold">Benvenuto in FoodAI</h1>
      <p className="mb-5">
        Pianifica i pasti per la tua giornata.
        ti chiederemo qualche informazione e il tuo obiettivo peso.
      </p>
      <Link to="/Calculator">
      <button className="btn btn-accent">Avvia</button>
      </Link>
    </div>
  </div>
</div>
    </>)
}