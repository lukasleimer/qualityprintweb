/* ============================================================================
   NAVIGATION INTERACTIONS
   ============================================================================
   
   Handles mobile navigation toggle and scroll effects.
   Progressive enhancement - works without JavaScript but enhanced with it.
   
============================================================================ */

'use strict';

(function() {
    // Configuration
    const SCROLL_THRESHOLD = 20;
    const SCROLL_CLASS = 'is-scrolled';
    
    // DOM Elements
    const navbar = document.querySelector('.navbar');
    const navToggle = document.getElementById('navbarToggle');
    const navMobile = document.getElementById('navbarMobile');
    const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    
    // Guard: Ensure elements exist
    if (!navbar || !navToggle || !navMobile) {
        console.warn('Navigation elements not found');
        return;
    }
    
    // ========================================================================
    // 1. MOBILE MENU TOGGLE
    // ========================================================================
    
    /**
     * Toggle mobile navigation menu
     */
    function toggleMobileMenu() {
        const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
        
        navToggle.setAttribute('aria-expanded', !isExpanded);
        navMobile.setAttribute('aria-hidden', isExpanded);
        
        if (!isExpanded) {
            // Opening menu
            document.body.style.overflow = 'hidden';
            navMobile.focus();
        } else {
            // Closing menu
            document.body.style.overflow = '';
            navToggle.focus();
        }
    }
    
    /**
     * Close mobile menu
     */
    function closeMobileMenu() {
        navToggle.setAttribute('aria-expanded', 'false');
        navMobile.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        navToggle.focus();
    }
    
    /**
     * Handle menu toggle click
     */
    navToggle.addEventListener('click', toggleMobileMenu);
    
    /**
     * Close menu when link is clicked
     */
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Only close if on mobile
            if (window.innerWidth < 768) {
                closeMobileMenu();
            }
        });
    });
    
    /**
     * Close menu on Escape key
     */
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
            if (isOpen) {
                closeMobileMenu();
            }
        }
    });
    
    /**
     * Close menu on outside click
     */
    document.addEventListener('click', (e) => {
        const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
        if (!navbar.contains(e.target) && isOpen) {
            closeMobileMenu();
        }
    });
    
    // ========================================================================
    // 2. STICKY NAVBAR SHADOW ON SCROLL
    // ========================================================================
    
    /**
     * Update navbar appearance on scroll
     */
    function handleScroll() {
        const scrolled = window.scrollY > SCROLL_THRESHOLD;
        
        if (scrolled) {
            navbar.classList.add(SCROLL_CLASS);
        } else {
            navbar.classList.remove(SCROLL_CLASS);
        }
    }
    
    // Add scroll listener with throttling
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
    
    // ========================================================================
    // 3. ACTIVE LINK DETECTION
    // ========================================================================
    
    /**
     * Detect current page and set active link
     */
    function setActiveLink() {
        const currentPath = window.location.pathname;
        
        // Get all nav links
        const allLinks = document.querySelectorAll('[data-active]');
        allLinks.forEach(link => link.removeAttribute('data-active'));
        
        // Set active based on current path
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            
            // Match current page
            if (href === currentPath || (currentPath === '/' && href === '/')) {
                link.setAttribute('data-active', 'true');
            } else if (href !== '/' && currentPath.startsWith(href)) {
                link.setAttribute('data-active', 'true');
            }
        });
    }
    
    // Set active link on page load
    setActiveLink();
    
    // ========================================================================
    // 4. RESIZE HANDLING
    // ========================================================================
    
    /**
     * Handle window resize
     */
    function handleResize() {
        // Close mobile menu if window becomes large enough for desktop
        if (window.innerWidth >= 768) {
            closeMobileMenu();
        }
    }
    
    // Add resize listener with throttling
    let resizeTicking = false;
    window.addEventListener('resize', () => {
        if (!resizeTicking) {
            window.requestAnimationFrame(() => {
                handleResize();
                resizeTicking = false;
            });
            resizeTicking = true;
        }
    }, { passive: true });
    
    // ========================================================================
    // 5. INITIALIZATION
    // ========================================================================
    
    // Initial setup
    document.addEventListener('DOMContentLoaded', () => {
        setActiveLink();
        handleScroll();
    });
    
    // Expose functions globally for debugging (optional)
    if (window.DEBUG) {
        window.navigation = {
            toggleMenu: toggleMobileMenu,
            closeMenu: closeMobileMenu,
            setActive: setActiveLink,
        };
    }
})();
