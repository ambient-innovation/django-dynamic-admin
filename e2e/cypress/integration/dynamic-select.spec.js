import { adminPaths } from "../support/paths";

context("Dynamic select", () => {
    before(() => {
        cy.visit(adminPaths.customerAdd);

        cy.get('input[name="username"]').type('SuperUser');
        cy.get('input[name="password"]').type('Admin123$');
        cy.get('form[method="post"]').submit();

        cy.location().should((loc) => {
            expect(loc.pathname).to.eq(adminPaths.customerAdd)
        })
    });

    after(() => {
        cy.visit(adminPaths.logout)
    });

    beforeEach(() => {
        Cypress.Cookies.preserveOnce("sessionid");
    });

    it("has dynamic employee selection", () => {
        cy.get('#id_district').select("District A/B")
        cy.get('#id_employee').should('have.value', '1')

        cy.get('#id_district').select("District C")
        cy.get('#id_employee').should('have.value', '3')
    })

    it("can hide fields according to selection", () => {
        cy.get('#id_lead_reason').select("TV")
        cy.get('#id_lead_reason_other').should('not.be.visible')

        cy.get('#id_lead_reason').select("Other")
        cy.get('#id_lead_reason_other').should('be.visible')
    })
})
