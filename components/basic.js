class server extends HTMLElement{
    constructor(){
        super();
        this.innerHTML = `
        <div id="server">
            <div id="cserver">
            <div id="cserver_name">Create Server</div>
            <div id="cserver_details">
                <input class="cserver_form" name="create_server_name" placeholder="Enter Server Name ">
                <select name="game" class="cserver_form">
                <option value="" disabled selected>Select game</option>
                <option value="uno">Uno</option>
                <option value="unonm">Uno Nomercy</option>
                <option value="poker">Poker</option>
                </select>
                <input type="checkbox" name="voicechat" class="cserver_form" >
                <label for="voicechat">Voice Chat</label>

                <input type="checkbox" name="message" class="cserver_form">
                <label for="message">Message</label>
                <button hx-post="/cserver_form" hx-swap="none" hx-include=".cserver_form ,#username">Create</button>
            </div>
            </div>
            <div id="jserver">
            <div id="jserver_name">Join Server</div>
            <div id="jserver_details">
                <input class="jserver_form" type="text" name="join_server_name" placeholder="Enter Server Name ">
                <button hx-post="/jserver_form" hx-swap="none" hx-include=".jserver_form ,#username">Join</button>

            </div>
            </div>
        </div>
        `;

    }
}

customElements.define('server-comp', server);