import React from 'react';
import test from './test.css'

export default class TopicHeader extends React.Component {
    render() {
        return (
            <header>
                <h3 className={test.h3}>Topic:{this.props.name}</h3>
            </header>
        );
    }
}
