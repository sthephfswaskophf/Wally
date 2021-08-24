import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-dep',
  templateUrl: './add-edit-dep.component.html',
  styleUrls: ['./add-edit-dep.component.css']
})
export class AddEditDepComponent implements OnInit {

  constructor(private service: SharedService) { }

  @Input() dep:any;
  DebtorId!: string;
  DebtorName!: string;



  ngOnInit(): void {
    this.DebtorId=this.dep.DebtorId;
    this.DebtorName=this.dep.DebtorName;

  }

  addDebtor(){
    var val = {DebtorId:this.DebtorId,
              DebtorName:this.DebtorName};
    this.service.addDebtor(val).subscribe(res=>{
      alert(res.toString());
    });

    }

  

  updateDebtor(){
    var val = {DebtorId:this.DebtorId,
              DebtorName:this.DebtorName};
    this.service.updateDebtor(val).subscribe(res=>{
      alert(res.toString());
    });
    
  }

}


