



export const ChatIA = ({ }) => {

    return (
        <>
            <div className="card card-compact bg-base-300 size-full shadow-xl">
                <div className="card size-full pb-8">
                    <div className="chat chat-start pt-8 pl-2">
                        <div className="chat-bubble chat-bubble-accent">
                            That's never been done in the history of the Jedi. It's insulting!
                        </div>
                    </div>
                    <div className="chat chat-end pt-8 pr-2">
                        <div className="chat-bubble chat-bubble-accent">
                            That's never been done in the history of the Jedi. It's insulting!
                        </div>
                    </div>
                </div>

                <div className="card bg-base-100 w-3/4 mx-auto  mb-4">
                    <div className="size-full px-8 py-8 flex">
                        <textarea className="textarea textarea-accent h-3 basis-3/4 " placeholder="Chatta con FoodAI"></textarea>
                        <button className="btn btn-accent basis-1/4 ml-4">send</button>
                    </div>
                </div>
            </div>


        </>
    )
}