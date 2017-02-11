import React from 'react';
import { Button,DatePicker } from 'antd'

export default class AntdDemo extends React.Component {
    render() {
        return (
            <header>
                <h3>AntdDemo</h3>
                <Button type="primary">Button</Button>
                <DatePicker />
            </header>
        );
    }
}
