import React from 'react';
import { Route } from 'react-router-dom';

import PrirodaList from './containers/PrirodaListView';
import PrirodaDetail from './containers/PrirodaDetailView';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component ={PrirodaList} />
        <Route exact path='/:prirodaID' component ={PrirodaDetail} />
    </div>
);

export default BaseRouter;