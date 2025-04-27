export function getAlimentMock (): Promise<{name: string,category:string,img : string,checked:boolean}[]>{
    return new Promise ((resolve)=>
    resolve(
        [
            {
                "name": "Latticini",
                "category": "dairy",
                "img": "https://i0.wp.com/www.fruitbookmagazine.it/wp-content/uploads/2020/12/Mele-Royal-Gala-bio.jpg?ssl=1",
                "checked": false
            }
            ,
            {
                "name": "Uova",
                "category": "eggs",
                "img": "https://i0.wp.com/www.fruitbookmagazine.it/wp-content/uploads/2020/12/Mele-Royal-Gala-bio.jpg?ssl=1",
                "checked": false
            },
            {
                "name": "zuppe e salse",
                "category": "soupsSauces",
                "img": "https://cdn.gvmnet.it/admingvm/media/immagininews/fegatostomacoeintestino/banane_benefici.jpeg",
                "checked": false
            },
            {
                "name": "Oli e grassi",
                "category": "oilsFats",
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4twRk5CYj0FFyVqDOy_BvAy5diBybtfU3mg&s",
                "checked": false
            },
            {
                "name": "Avicoli",
                "category": "poultry",
                "img": "https://galleria.riza.it/files/article/fragola-buona-e-salutare.jpg",
                "checked": false
            },
            {
                "name": "Carne",
                "category": "meats",
                "img": "https://www.my-personaltrainer.it/2019/10/19/pere_900x760.jpeg",
                "checked": false
            },
            {
                "name": "Cereali",
                "category": "cereals",
                "img": "https://www.nutrizionistacristinamucci.it/wp-content/uploads/2019/11/uva-terzo-post.jpg",
                "checked": false
            },
            {
                "name": "Frutta",
                "category": "fruits",
                "img": "https://www.nonsprecare.it/wp-content/uploads/2017/11/proprieta-benefici-ananas-2.jpg",
                "checked": false
            },
            {
                "name": "Verdura",
                "category": "vegetables",
                "img": "https://campaniatradizione.it/wp-content/uploads/2021/06/ciliegie-biologiche-di-campania-tradizione-1.jpg",
                "checked": false
            }
        ]
        
    
))

}