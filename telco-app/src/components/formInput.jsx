import React, { Component } from 'react';
import ContainerMd from './containerMd';
import Input from './input';

class FormInput extends Component {
    render(props) { 
        const { onChange, input, onSubmit } = this.props;
        return (
        <ContainerMd>
            <Input 
                onChange={onChange}
                onSubmit={onSubmit}
                input={input}
            />
        </ContainerMd>);
    }
}
 
export default FormInput;