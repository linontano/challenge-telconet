import React, { Component } from 'react';
class Input extends Component {
    render() { 
        const { input, onChange, onSubmit } = this.props
        return (
            <form className="input-group my-3" onSubmit={onSubmit}>
                <input required type="text" className="form-control" placeholder="Ingrese red a consultar" value={input} onChange={onChange} pattern="^((\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$"/>
                <div className="input-group-append">
                    <input className="btn btn-outline-secondary" type="submit" value="Consultar" />
                </div>
            </form>
        );
    }
};
export default Input;