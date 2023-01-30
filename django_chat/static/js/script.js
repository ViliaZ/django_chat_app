

async function sendMessage() {
    let message = messagefield.value; // input from HTML
    let messageTime = getFormattedDate();
    let token = '{{ csrf_token }}'; // use django variable

    let formdata = new FormData();
    formdata.append('textmessage', message);
    formdata.append('csrfmiddlewaretoken', token);

    // render preview message from JS data only
    messageContainer.innerHTML += `
        <div id="tempMessage" class="message grey">
          <span>[ ${ messageTime } ]</span>
          {{ request.user.first_name }}:
          <i>${ message }</i>
        </div>
    `
    try {
        result = await fetch('/chat/',{
            method: 'POST',
            body: formdata
        })
        messageAsJson = await result.json();
        // remove preview message
        tempMessage.remove();
        // render final message after backend response
        messageContainer.innerHTML += `
        <div id="tempMessage" class="message">
          <span>[ ${ messageAsJson.fields.created_at } ]</span>
          {{ messageAsJson.fields.author }}:
          <i>${ messageAsJson.fields.text }</i>
        </div>
    `

    } catch (e) {
        console.error('Could not post the message to backend, an error occurred:', e)
    }
}

function getFormattedDate() {
    console.log("formatted date")
  let now = new Date();
  let targetFormat = 'mm. dd, yy'
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  
  const map = {
    hh: now.getHours(),
    mm: now.getMinutes(),
    ss: now.getSeconds(),
    dd: now.getDate(),
    mm: months[now.getMonth()], 
    yy: now.getFullYear()
  }
  let formattedDate = targetFormat.replace(/mm|dd|yy/gi, matched => map[matched]);
  return formattedDate;
}