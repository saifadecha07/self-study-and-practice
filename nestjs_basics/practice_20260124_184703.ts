// Session: Morning study session
// Note: Need to memorize this syntax.

import { Controller, Get, Post, Body } from '@nestjs/common';

// Source: NestJS Official Documentation - Controllers
@Controller('cats')
export class CatsController {
  @Post()
  create(@Body() createCatDto: any) {
    return 'This action adds a new cat';
  }

  @Get()
  findAll(): string {
    return 'This action returns all cats';
  }
}