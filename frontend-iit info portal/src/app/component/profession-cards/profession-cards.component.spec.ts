import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfessionCardsComponent } from './profession-cards.component';

describe('ProfessionCardsComponent', () => {
  let component: ProfessionCardsComponent;
  let fixture: ComponentFixture<ProfessionCardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfessionCardsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfessionCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
