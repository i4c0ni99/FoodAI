export function getAlimentMock (): Promise<{name: string,category:string,img : string,checked:boolean}[]>{
    return new Promise ((resolve)=>
    resolve(
        [
            {
                "name": "Latticini",
                "category": "dairy",
                "img": "https://www.fondazioneveronesi.it/uploads/thumbs/2020/01/16/latte-latticini-dieta_thumb_720_480.jpg",
                "checked": false
            }
            ,
            {
                "name": "Uova",
                "category": "eggs",
                "img": "https://www.curarsiconilcibo.com/wp-content/uploads/2021/03/UOVA.jpg",
                "checked": false
            },
            {
                "name": "Oli e grassi",
                "category": "oilsFats",
                "img": "https://www.my-personaltrainer.it/2023/07/21/colesterolo-oli-e-grassi-orig.jpeg",
                "checked": false
            },
            {
                "name": "Avicoli",
                "category": "poultry",
                "img": "https://www.chiappinellicarni.it/it/wp-content/uploads/2019/02/Le-vendite-della-carne-di-pollo-sorpassano-quelle-del-bovino-1-1.jpg",
                "checked": false
            },
            {
                "name": "Carne",
                "category": "meats",
                "img": "https://www.my-personaltrainer.it/2023/10/31/carne-orig.jpegg",
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
            },
            {
                "name": "Legumi",
                "category": "legumes",
                "img": "https://campaniatradizione.it/wp-content/uploads/2021/06/ciliegie-biologiche-di-campania-tradizione-1.jpg",
                "checked": false
            },
            {
                "name": "Pesce",
                "category": "fish",
                "img": "https://campaniatradizione.it/wp-content/uploads/2021/06/ciliegie-biologiche-di-campania-tradizione-1.jpg",
                "checked": false
            },
            {
                "name": "Primi piatti",
                "category": "first dishes",
                "img": "https://campaniatradizione.it/wp-content/uploads/2021/06/ciliegie-biologiche-di-campania-tradizione-1.jpg",
                "checked": false
            },
            {
                "name": "Frutta secca",
                "category": "nutsAndSeeds",
                "img": "https://campaniatradizione.it/wp-content/uploads/2021/06/ciliegie-biologiche-di-campania-tradizione-1.jpg",
                "checked": false
                
            }
        ]
        
    
))

}