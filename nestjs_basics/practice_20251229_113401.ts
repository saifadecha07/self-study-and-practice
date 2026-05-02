// Session: Lunch break learning
// Note: Finally understood this concept!

import { Injectable } from '@nestjs/common';

// Source: NestJS Official Documentation - Providers
export interface Cat { name: string; age: number; breed: string; }

@Injectable()
export class CatsService {
  private readonly cats: Cat[] = [];

  create(cat: Cat) {
    this.cats.push(cat);
  }

  findAll(): Cat[] {
    return this.cats;
  }
}