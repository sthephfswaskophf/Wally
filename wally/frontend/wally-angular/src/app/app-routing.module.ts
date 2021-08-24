import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EmployeeComponent } from './employee/employee.component';
import { DebtorComponent } from './debtor/debtor.component';

const routes: Routes = [
  {path:'employee',component:EmployeeComponent},
  {path:'debtor',component:DebtorComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
