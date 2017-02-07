import { Button } from 'antd';
import React from 'react';
//import button from './button.css'

export default class AntButtons extends React.Component {
    render() {
        return (
          <div>
            <Button type="primary">Primary</Button>
            <Button>Default</Button>
            <Button type="dashed">Dashed</Button>
            <Button type="danger">Danger</Button>
          </div>
        );
    }
}
