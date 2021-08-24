import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {

  constructor(private service: SharedService) { }

  DebtorList: any=[];

  ModalTitle!: string;
  ActivateAddEditDepComp:boolean=false;
  dep:any;

  ngOnInit(): void {
    this.refreshDepList();

  }

  addClick(){
    this.dep={
      IdDebtor:0,
      name:""
    }

    this.ModalTitle="Adicionar Devedor";
    this.ActivateAddEditDepComp=true;

  }

 editClick(item: any){
   this.dep=item;
   this.ModalTitle="Editar Devedor";
   this.ActivateAddEditDepComp=true;


 }



  closeClick(){
    this.ActivateAddEditDepComp=false;
    this.refreshDepList();
  }



  refreshDepList(){
    this.service.getDepList().subscribe(data=>{
      this.DebtorList=data;

    });
  }

}
