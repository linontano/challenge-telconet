import React, { Component } from 'react';
class ContainerMd extends Component {
    render() { 
        const { children } = this.props
        return (
        <div className="container-md">
            { children }
        </div>
        );
    }
}
 
export default ContainerMd;