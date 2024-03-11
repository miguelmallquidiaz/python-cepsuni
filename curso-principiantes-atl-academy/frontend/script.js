//Cuando cargue completamente la página web va a ejecutar la función search
document.addEventListener("DOMContentLoaded", init);
const URL_API = 'http://localhost:3000/api/'

var customers = []

function init() {
    search()
}

function addCustomer(){
    clean()
    openModal()
}

function openModal() {
    let htmlModal = document.getElementById('modal')
    //Agregar un elemento a la class
    htmlModal.classList.add('opened')
  }
  
  function closeModal() {
    let htmlModal = document.getElementById('modal')
    //Agregar un elemento a la class
    htmlModal.classList.remove('opened')
  }

async function search() {
    //fech va a traer de esta url como hacer una request
    var url = URL_API + 'customers'
    var response =  await fetch(url,  {
        "method": 'GET',
        "headers":{
            "Content-Type": 'application/json'
            }
        });
    //convertir la respuesta a json
    customers = await response.json();

    var html = ''
    for(customer of customers) {
        var row = `
        <tr>
            <td>${customer.firstname}</td>
            <td>${customer.lastname}</td>
            <td>${customer.email}</td>
            <td>${customer.phone}</td>
            <td>
                <button onclick="edit(${customer.id})" class="css-button css-button-3d css-button-3d--yellow">Editar</button>
                <button onclick="remove(${customer.id})" class="css-button css-button-3d css-button-3d--red">Eliminar</button>
            </td>
        </tr>
        `
        html += row;
    }
    
    document.querySelector('#customers > tbody').outerHTML = html
}

async function remove(id) {
    respuesta = confirm('¿Estas seguro de eliminarlo?')
    if(respuesta){
        //fech va a traer de esta url como hacer una request
        var url = URL_API + 'customers/' + id
        await fetch(url,  {
        "method": 'DELETE',
        "headers":{
            "Content-Type": 'application/json'
            }
        });
        window.location.reload()
    }
}

async function edit(id) {
    openModal()
    var customer = customers.find(x => x.id == id)
    document.getElementById('txtId').value = customer.id
    document.getElementById('txtFirstname').value = customer.firstname
    document.getElementById('txtLastname').value = customer.lastname
    document.getElementById('txtPhone').value = customer.phone
    document.getElementById('txtEmail').value = customer.email
}

async function saveCustomer() {
    var data = {
        "email": document.getElementById('txtEmail').value,
        "firstname": document.getElementById('txtFirstname').value,
        "lastname": document.getElementById('txtLastname').value,
        "phone": document.getElementById('txtPhone').value
    }

    var id = document.getElementById('txtId').value
    if(id != ''){
        data.id = id
    }
    //fech va a traer de esta url como hacer una request
    var url = URL_API + 'customers'
    await fetch(url,  {
    "method": 'POST',
    "body": JSON.stringify(data),
    "headers":{
        "Content-Type": 'application/json'
        }
    });
    window.location.reload()
}

function clean(){
    document.getElementById('txtId').value = ''
    document.getElementById('txtFirstname').value = ''
    document.getElementById('txtLastname').value = ''
    document.getElementById('txtPhone').value = ''
    document.getElementById('txtEmail').value = ''
}