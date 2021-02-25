import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ProductListComponent } from './components/product-list/product-list.component';
import { ProductAddComponent } from './components/product-add/product-add.component';
import { ProductManageComponent } from './components/product-manage/product-manage.component';
import { ProductDetailComponent } from './components/product-detail/product-detail.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import {AuthGuard} from './helpers/auth.guard';
import {UserListComponent} from './components/user-list/user-list.component';
import {UserDetailComponent} from './components/user-detail/user-detail.component';


const routes: Routes = [
  { path: 'api/products', component: ProductListComponent },
  { path: 'api/manage/add', component: ProductAddComponent, canActivate: [AuthGuard] },
  { path: 'api/manage/:productSlug', component: ProductDetailComponent, canActivate: [AuthGuard] },
  { path: 'api/manage', component: ProductManageComponent, canActivate: [AuthGuard] },
  { path: 'api/login', component: LoginComponent },
  { path: 'api/register', component: RegisterComponent },
  { path: 'api/users/:id', component: UserDetailComponent },
  { path: 'api/users', component: UserListComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
