import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from "../../types";

describe('ProductCard test', () => {


    it('should render correctly', () => {
        const product: Product = {
        id: 1,
        name: 'test',
        description: 'testing',
        price: 123,
        priceSymbol: '₽',
        category: 'Одежда',
        imgUrl: "/test.png"
        };
        const { asFragment } = render(<ProductCard {...product} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should render correctly without price symbol', () => {
        const product: Product = {
        id: 1,
        name: 'test',
        description: 'testing',
        price: 123,
        category: 'Одежда',
        imgUrl: "/test.png"
        };
        const { asFragment } = render(<ProductCard {...product} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should render correctly with different price symbols', () => {
        const product: Product = {
          id: 1,
          name: 'test',
          description: 'testing',
          price: 123,
          priceSymbol: '$',
          category: 'Одежда',
        };
        const { asFragment } = render(<ProductCard {...product} />);
        expect(asFragment()).toMatchSnapshot();
    });

    it('should not render image when imgUrl is undefined', () => {
        const product: Product = {
            id: 1,
            name: 'test',
            description: 'testing',
            price: 123,
            priceSymbol: '₽',
             category: 'Одежда',
             imgUrl: undefined,
        };
        const { queryByText } = render(<ProductCard {...product} />);
        expect(queryByText('img')).toBeNull();
    });
});