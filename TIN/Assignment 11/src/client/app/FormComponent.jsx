import React from 'react';
import TextDisplayComponent from './TextDispComponent.jsx';
import LabelValueComponent from './LabelValueComponent.jsx';

class FirstForm extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            description: "",
            hours: 0,
            email: "",
            messageForDescription: "Description is too short",
            messageForHours: "Number of hours is too big",
            messageForEmail: "Email is wrong",
            isDescValid: false,
            isHoursValid: false,
            isEmailValid: false
        }
    }

    descriptionHandleChange(event) {
        let val = event.target.value;
        if (val.length < 10) {
            this.setState({ description: val , messageForDescription: "Description is too short" , isDescValid: false});
        } else{
            this.setState({ description: val , messageForDescription: "", isDescValid: true });
        }

    }

    hoursHandleChange(event) {
        let val = event.target.value;
        if (val > 8 || val == "") {
            this.setState({ hours: val , messageForHours: "Number of hours is too big", isHoursValid: false });
        } else{
            this.setState({ hours: val , messageForHours: "" , isHoursValid: true});
        }
    }

    emailHandleChange(event) {

        let val = event.target.value;
        let pattern = new RegExp("[a-zA-z0-9]+@gmail.com");
        if (!pattern.test(val)) {
            this.setState({ email: val , messageForEmail: "Email is wrong", isEmailValid: false });
        } else{
            this.setState({ email: val , messageForEmail: "", isEmailValid: true });
        }
    }

    render() {
        return <div>
            <form>
                <label htmlFor='description'>Description: </label>
                <input type="text" name="description" id="description" value={this.state.description}
                    onChange={this.descriptionHandleChange.bind(this)}></input> 
                <TextDisplayComponent class="invalid" text={this.state.messageForDescription}></TextDisplayComponent><br/>
                <label htmlFor='hours'>Hours: </label>
                <input type="number" name="hours" id='hours' value={this.state.hours}
                    onChange={this.hoursHandleChange.bind(this)}></input>
                <TextDisplayComponent class="invalid"  text={this.state.messageForHours}></TextDisplayComponent><br/>
                <label htmlFor='email'>Email: </label>
                <input type="email" name='email' id='email' value={this.state.email}
                    onChange={this.emailHandleChange.bind(this)}></input>
                <TextDisplayComponent class="invalid"  text={this.state.messageForEmail }></TextDisplayComponent><br/>
                <LabelValueComponent class={this.state.isDescValid ? "valid" : "invalid"} label="Is description field valid" val={this.state.isDescValid ? "true" : "false"} ></LabelValueComponent>
                <LabelValueComponent class={this.state.isHoursValid ? "valid" : "invalid"} label="Is hours field valid" val={this.state.isHoursValid ? "true" : "false"} ></LabelValueComponent>
                <LabelValueComponent class={this.state.isEmailValid ? "valid" : "invalid"} label="Is email field valid" val={this.state.isEmailValid ? "true" : "false"} ></LabelValueComponent>
            </form>
        </div>
    }
}

export default FirstForm;