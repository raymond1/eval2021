document.getElementById('lookup_button').onclick = ()=>{
  //alert(document.getElementById('address').value)
  //document.getElementById('display_area').innerHTML = '12345'

  const request = new Request('/api/lookup/' + document.getElementById('address').value);
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
}


// address = json['address']
// balance = json['balance']
// final_balance = json['final_balance']
// final_n_tx = json['final_n_tx']
// n_tx = json['n_tx']
// total_received = json['total_received']
// total_sent = json['total_sent']
// unconfirmed_balance = json['unconfirmed_balance']
// unconfirmed_n_tx = json['unconfirmed_n_tx']
