const SpinnerBox = document.getElementById('spinner-box')
const dataBox = document.getElementById('data-box')
const linkStatus = document.getElementById('status')

/* SpinnerBox.style.display = "none" */
function statusWhatsApp(){
    SpinnerBox.style.display = "block"
    $.ajax({
        type: 'GET',
        url: '/wp/status/',
        success: function(response){            
            SpinnerBox.style.display = "none"            
            if(response['status'] == 'logout'){
                dataBox.innerHTML += '<h5>Por favor faça o login</h5>'                
                dataBox.innerHTML += '<img src="/static/image.png"/>'                
                dataBox.innerHTML += '<span style="color:red">Atualize a página assim que conectar o whatsapp</span>'                
                linkStatus.style.display = 'none'             
            }else{
                dataBox.innerHTML += '<h5 style="color:green">O whatsapp está logado no servidor</h5>'
                linkStatus.style.display = 'none'
            }
        }, 
        error: function(response){
            alert('errro')
        }
    })
}

statusWhatsApp()