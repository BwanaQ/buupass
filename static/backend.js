bus_registration = document.getElementsByClassName('bus-registration').id;
console.log(bus-registration)

all_seats = document.querySelector('.row .seat')


async function contactAPI(url,body){
    const response= await fetch(url,{
        method: 'POST',
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify (body)
    })
    return response.json()
}

function refreshSeat(){

}

