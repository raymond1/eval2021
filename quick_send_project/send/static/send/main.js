let load_address_information = ()=>{
  //alert(document.getElementById('address').value)
  //document.getElementById('display_area').innerHTML = '12345'

  const request = new Request('/api/lookup/' + document.getElementById('address').value)
  fetch(request).then(response => response.json()).then(
    (data)=>{
      output_string = ''
      fields = ['address','balance','final_balance','final_n_tx','n_tx','total_received','total_sent','unconfirmed_balance','unconfirmed_n_tx']
      for (let field of fields){
        output_string += field + ' = ' + data[field] + '\n'
        console.log(data[field])
      }
      document.getElementById('display_area').innerHTML = output_string
//      alert(JSON.stringify(data))
    }
  )

  const request2 = new Request('/api/generate_qr_code/' + document.getElementById('address').value)
  fetch(request2).then(
    response => response.blob().then(
      (data)=>{
        let qr_code_image_url = window.URL.createObjectURL(data)
        debugger
        document.getElementById('qr_code').innerHTML = "<img src='" + qr_code_image_url + "' alt='QR code'>"
      }
    )  
  )
}

document.getElementById('lookup_button').onclick = load_address_information

load_address_information()
